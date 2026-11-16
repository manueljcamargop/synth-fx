/*
 * MJ Reverb · motor de reverberación para la web (Synth FX).
 *
 * Traducción línea a línea de MJReverbCore.h y MJReverbParams.h, el motor del
 * plugin VST3 MJ Reverb. Con los mismos valores de las perillas, la web y el
 * plugin producen la misma señal (verificado muestra a muestra en las pruebas).
 * Si cambias algo aquí, cámbialo también en el C++.
 *
 * Se usa de dos formas:
 *  - En la página, como <script src="mjreverb-core.js">: expone window.MJReverb
 *    (rangos, recorrido de perillas, cálculo de reflexiones) para dibujar.
 *  - Dentro de un AudioWorklet: la página copia el código de este archivo al
 *    worklet (MJReverb.workletSource()), así funciona también sin servidor.
 */
(function () {
function mjreverbFactory(root) {
  'use strict';

  // ---- Rangos y parámetros (MJReverbParams.h) ----
  const R = (min, max, def) => ({ min, max, def });
  const RANGES = {
    preDelayMs: R(0, 250, 20), decayS: R(0.2, 10, 1.8), mixPct: R(0, 100, 30),
    widthPct: R(0, 100, 100), earlyPct: R(0, 100, 50), heightM: R(2, 20, 4),
    roomWidthM: R(2, 50, 10), depthM: R(2, 60, 15), materialPct: R(0, 100, 55)
  };
  const SPECS = [
    { key: 'preDelayMs',  label: 'PRE-DELAY',   name: 'Pre-delay',              units: 'ms', scale: 'lin', precision: 0, desc: 'Hueco antes de la cola' },
    { key: 'decayS',      label: 'DECAY',       name: 'Decay (RT60)',           units: 's',  scale: 'log', precision: 2, desc: 'Cuánto dura la cola (RT60)' },
    { key: 'earlyPct',    label: 'REFLEXIONES', name: 'Reflexiones tempranas',  units: '%',  scale: 'lin', precision: 0, desc: 'Primeros rebotes en las paredes' },
    { key: 'widthPct',    label: 'ESTÉREO',     name: 'Estéreo',                units: '%',  scale: 'lin', precision: 0, desc: 'Apertura de la reverb' },
    { key: 'mixPct',      label: 'MEZCLA',      name: 'Mezcla',                 units: '%',  scale: 'lin', precision: 0, desc: 'Seco ↔ reverberante' },
    { key: 'heightM',     label: 'ALTO',        name: 'Alto de la sala',        units: 'm',  scale: 'log', precision: 1, desc: 'Del piso al techo' },
    { key: 'roomWidthM',  label: 'ANCHO',       name: 'Ancho de la sala',       units: 'm',  scale: 'log', precision: 1, desc: 'De pared a pared' },
    { key: 'depthM',      label: 'PROFUNDIDAD', name: 'Profundidad de la sala', units: 'm',  scale: 'log', precision: 1, desc: 'Del frente al fondo' },
    { key: 'materialPct', label: 'MATERIAL',    name: 'Material',               units: '%',  scale: 'lin', precision: 0, desc: 'Absorbente ↔ reflectante' }
  ];
  const SPEED_OF_SOUND = 343, MAX_EARLY_S = 0.75;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));

  function toPlain(spec, norm) {
    const r = RANGES[spec.key], n = clamp(norm, 0, 1);
    return spec.scale === 'log' ? r.min * Math.pow(r.max / r.min, n) : r.min + (r.max - r.min) * n;
  }
  function toNormalized(spec, plain) {
    const r = RANGES[spec.key], v = clamp(plain, r.min, r.max);
    return spec.scale === 'log' ? Math.log(v / r.min) / Math.log(r.max / r.min) : (v - r.min) / (r.max - r.min);
  }
  function defaults() { const p = {}; for (const k in RANGES) p[k] = RANGES[k].def; return p; }

  const materialReflectance = (m) => 0.4 + 0.55 * m / 100;
  const materialHighRatio = (m) => 0.3 + 0.65 * m / 100;
  function materialName(m) {
    return m < 20 ? 'Cortina' : m < 40 ? 'Alfombra' : m < 60 ? 'Madera' : m < 80 ? 'Yeso' : 'Concreto';
  }

  // Posiciones fijas de fuente y oyente (fracciones de la sala), iguales a las del C++.
  function positions(W, H, D) {
    const h = Math.min(1.5, 0.45 * H);
    return { src: { x: 0.27 * W, y: h, z: 0.62 * D }, ear: { x: 0.72 * W, y: h, z: 0.35 * D } };
  }

  // Reflexiones tempranas por fuentes espejo (1.º y 2.º orden). computeEarlyTaps del C++.
  function computeEarlyTaps(W, H, D, materialPct) {
    const { src, ear } = positions(W, H, D);
    const hyp3 = (a, b, c) => Math.hypot(Math.hypot(a, b), c);
    const direct = hyp3(ear.x - src.x, ear.y - src.y, ear.z - src.z);
    const refl = materialReflectance(materialPct);
    const images = (s, L) => [[s, 0], [-s, 1], [2 * L - s, 1], [s - 2 * L, 2], [2 * L + s, 2]];
    const taps = [];
    for (const [ix, ox] of images(src.x, W))
      for (const [iy, oy] of images(src.y, H))
        for (const [iz, oz] of images(src.z, D)) {
          const order = ox + oy + oz;
          if (order < 1 || order > 2) continue;
          const dist = hyp3(ear.x - ix, ear.y - iy, ear.z - iz);
          const delayMs = (dist - direct) / SPEED_OF_SOUND * 1000;
          if (delayMs <= 0 || delayMs > MAX_EARLY_S * 1000) continue;
          const g = Math.pow(refl, order) * direct / dist;
          const p = clamp((ix - ear.x) / Math.max(dist, 0.001), -1, 1);
          const ang = (p + 1) * 0.78539816;
          taps.push({ delayMs, gainL: g * Math.cos(ang) * 1.41421356, gainR: g * Math.sin(ang) * 1.41421356, order, x: ix, y: iy, z: iz });
        }
    taps.sort((a, b) => a.delayMs - b.delayMs);
    return taps;
  }

  function dampingCoeff(r, w0, wHigh) {
    if (r >= 0.9999) return 0;
    const mag = (a, w) => (1 - a) / Math.sqrt(1 - 2 * a * Math.cos(w) + a * a);
    let lo = 0, hi = 0.999;
    for (let i = 0; i < 40; ++i) {
      const a = 0.5 * (lo + hi);
      if (mag(a, wHigh) / mag(a, w0) > r) lo = a; else hi = a;
    }
    return 0.5 * (lo + hi);
  }

  // ---- Procesamiento (ReverbCore) ----
  class DelayLine {
    resize(maxSamples) { let n = 1; while (n < maxSamples + 2) n <<= 1; this.buf = new Float32Array(n); this.mask = n - 1; this.w = 0; }
    clear() { this.buf.fill(0); this.w = 0; }
    write(x) { this.buf[this.w] = x; this.w = (this.w + 1) & this.mask; }
    read(d) {
      const rp = this.w - d, i0 = Math.floor(rp), f = rp - i0;
      const a = this.buf[i0 & this.mask], b = this.buf[(i0 + 1) & this.mask];
      return a + (b - a) * f;
    }
    readInt(d) { return this.buf[(this.w - d) & this.mask]; }
  }
  class Allpass {
    init(d, g) { this.d = d; this.g = g; this.line = new DelayLine(); this.line.resize(d + 1); }
    clear() { this.line.clear(); }
    process(x) { const z = this.line.readInt(this.d), v = x + this.g * z; this.line.write(v); return z - this.g * v; }
  }
  class Smoothed {
    constructor() { this.cur = 0; this.target = 0; this.coeff = 0; }
    setTime(sr, ms) { this.coeff = Math.exp(-1 / (0.001 * ms * sr)); }
    snap(v) { this.cur = this.target = v; }
    next() { this.cur = this.target + (this.cur - this.target) * this.coeff; return this.cur; }
  }

  const LINES = 8, MAX_TAPS = 24;
  const BASE = [1399, 1777, 2063, 2399, 2789, 3209, 3709, 4603], AP = [142, 107, 379, 277];

  class ReverbCore {
    constructor() {
      this.sr = 0; this.p = defaults();
      this.lines = Array.from({ length: LINES }, () => new DelayLine());
      this.len = new Int32Array(LINES); this.gain = new Float64Array(LINES); this.damp = new Float64Array(LINES); this.lp = new Float64Array(LINES);
      this.diff = Array.from({ length: 4 }, () => new Allpass());
      this.pre = new DelayLine(); this.early = new DelayLine();
      this.mix = new Smoothed(); this.width = new Smoothed(); this.earlyG = new Smoothed(); this.preD = new Smoothed();
      this.tapD = new Float64Array(MAX_TAPS); this.tapGL = new Float64Array(MAX_TAPS); this.tapGR = new Float64Array(MAX_TAPS);
      this.numTaps = 0; this.phase = 0; this.y = new Float64Array(LINES);
    }
    modDepthSamples() { return Math.max(1, Math.round(0.0006 * this.sr)); }
    prepare(sampleRate) {
      this.sr = sampleRate; const k = this.sr / 48000;
      for (let i = 0; i < LINES; ++i) { this.len[i] = Math.max(8, Math.round(BASE[i] * k)); this.lines[i].resize(this.len[i] + this.modDepthSamples() + 4); }
      for (let i = 0; i < 4; ++i) this.diff[i].init(Math.max(2, Math.round(AP[i] * k)), 0.62);
      this.pre.resize(Math.ceil(RANGES.preDelayMs.max * 0.001 * this.sr) + 4);
      this.early.resize(Math.ceil(MAX_EARLY_S * this.sr) + 4);
      this.mix.setTime(this.sr, 30); this.width.setTime(this.sr, 30); this.earlyG.setTime(this.sr, 30); this.preD.setTime(this.sr, 60);
      this.setParams(this.p);
      for (const s of [this.mix, this.width, this.earlyG, this.preD]) s.snap(s.target);
      this.reset();
    }
    reset() { for (const l of this.lines) l.clear(); for (const a of this.diff) a.clear(); this.pre.clear(); this.early.clear(); this.lp.fill(0); this.phase = 0; }
    setParams(np) {
      const p = this.p;
      for (const key in RANGES) if (np[key] !== undefined) p[key] = clamp(Number(np[key]), RANGES[key].min, RANGES[key].max);
      if (this.sr <= 0) return;
      this.mix.target = p.mixPct / 100; this.width.target = p.widthPct / 100; this.earlyG.target = p.earlyPct / 100;
      this.preD.target = Math.max(1, p.preDelayMs * 0.001 * this.sr);
      const taps = computeEarlyTaps(p.roomWidthM, p.heightM, p.depthM, p.materialPct);
      this.numTaps = Math.min(MAX_TAPS, taps.length);
      for (let i = 0; i < MAX_TAPS; ++i) {
        if (i < this.numTaps) { this.tapD[i] = Math.max(1, taps[i].delayMs * 0.001 * this.sr); this.tapGL[i] = taps[i].gainL; this.tapGR[i] = taps[i].gainR; }
        else { this.tapD[i] = 1; this.tapGL[i] = this.tapGR[i] = 0; }
      }
      const w500 = 2 * Math.PI * 500 / this.sr, w4k = 2 * Math.PI * Math.min(4000, 0.4 * this.sr) / this.sr;
      const highRatio = materialHighRatio(p.materialPct);
      for (let i = 0; i < LINES; ++i) {
        const L = this.len[i];
        const gMid = Math.pow(10, -3 * L / (this.sr * p.decayS)), gHigh = Math.pow(10, -3 * L / (this.sr * p.decayS * highRatio));
        const a = dampingCoeff(gHigh / gMid, w500, w4k);
        const magMid = (1 - a) / Math.sqrt(1 - 2 * a * Math.cos(w500) + a * a);
        this.damp[i] = a; this.gain[i] = gMid / magMid;
      }
    }
    process(inL, inR, outL, outR, n) {
      const twoPi = 6.283185307, modRate = 0.31 / this.sr, depth = this.modDepthSamples();
      const lines = this.lines, len = this.len, gain = this.gain, damp = this.damp, lp = this.lp, y = this.y;
      for (let s = 0; s < n; ++s) {
        const xl = inL[s], xr = inR[s], xm = 0.5 * (xl + xr);
        this.pre.write(xm);
        const pd = this.pre.read(this.preD.next());
        this.early.write(pd);
        let eL = 0, eR = 0;
        for (let k = 0; k < this.numTaps; ++k) { const v = this.early.read(this.tapD[k]); eL += this.tapGL[k] * v; eR += this.tapGR[k] * v; }
        const eg = this.earlyG.next() * 0.6; eL *= eg; eR *= eg;
        let d = pd;
        for (const a of this.diff) d = a.process(d);
        this.phase += modRate; if (this.phase >= 1) this.phase -= 1;
        for (let i = 0; i < LINES; ++i) {
          let del = len[i];
          if (i === 1) del += depth * (0.5 + 0.5 * Math.sin(twoPi * this.phase));
          if (i === 6) del += depth * (0.5 + 0.5 * Math.cos(twoPi * this.phase * 1.37));
          const v = lines[i].read(del) * gain[i];
          lp[i] = (1 - damp[i]) * v + damp[i] * lp[i];
          y[i] = lp[i];
        }
        for (let h = 1; h < LINES; h <<= 1)
          for (let i = 0; i < LINES; i += h << 1)
            for (let j = i; j < i + h; ++j) { const a = y[j], b = y[j + h]; y[j] = a + b; y[j + h] = a - b; }
        for (let i = 0; i < LINES; ++i) lines[i].write(y[i] * 0.35355339 + ((i & 1) ? -d : d) * 0.25);
        let tL = 0, tR = 0;
        for (let i = 0; i < LINES; ++i) { const v = lp[i]; tL += (i % 4 < 2) ? v : -v; tR += (i % 2 === 0) ? v : -v; }
        tL *= 0.30; tR *= 0.30;
        let wL = eL + tL, wR = eR + tR;
        const w = this.width.next(), mid = 0.5 * (wL + wR), side = 0.5 * (wL - wR) * w;
        wL = mid + side; wR = mid - side;
        const m = this.mix.next();
        outL[s] = xl * (1 - m) + wL * m;
        outR[s] = xr * (1 - m) + wR * m;
      }
    }
  }

  // Código del AudioWorklet: este mismo archivo + un procesador que usa ReverbCore.
  const WORKLET_TAIL = `
    class MJReverbProcessor extends AudioWorkletProcessor {
      constructor(options) {
        super();
        this.core = new MJReverb.ReverbCore();
        // Los valores iniciales llegan al crear el nodo, así el primer bloque ya suena bien.
        const init = options && options.processorOptions && options.processorOptions.params;
        if (init) this.core.setParams(init);
        this.core.prepare(sampleRate);
        this.port.onmessage = (e) => { if (e.data && e.data.params) this.core.setParams(e.data.params); if (e.data && e.data.reset) this.core.reset(); };
      }
      process(inputs, outputs) {
        const input = inputs[0], output = outputs[0];
        const n = output[0].length;
        const inL = input && input[0] ? input[0] : new Float32Array(n);
        const inR = input && input[1] ? input[1] : inL;
        this.core.process(inL, inR, output[0], output[1] || new Float32Array(n), n);
        return true;
      }
    }
    registerProcessor('mjreverb', MJReverbProcessor);`;

  const api = {
    RANGES, SPECS, SPEED_OF_SOUND, toPlain, toNormalized, defaults, positions,
    computeEarlyTaps, materialReflectance, materialHighRatio, materialName, ReverbCore,
    // El worklet recibe el código de esta misma fábrica, así no depende de cargar archivos.
    workletSource() { return '(' + mjreverbFactory.toString() + ')(globalThis);' + WORKLET_TAIL; }
  };
  root.MJReverb = api;
  return api;
}
const api = mjreverbFactory(typeof globalThis !== 'undefined' ? globalThis : this);
if (typeof module !== 'undefined' && module.exports) module.exports = api;
})();
