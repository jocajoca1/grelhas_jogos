const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 900, height: 1200 } });
  await p.goto('file://' + __dirname + '/pulso_enigmas.html', { waitUntil: 'networkidle' });
  await p.waitForFunction(() => document.body.dataset.fitted === '1');
  console.log(await p.$$eval('.page', ps => ps.map(x => x.dataset.fs).join(' ')));
  // verificar transbordo de cada página
  const over = await p.$$eval('.page', ps => ps.map((el, i) => {
    const r = el.getBoundingClientRect(); let maxB = 0;
    el.querySelectorAll('*').forEach(c => { if (c.closest('.foot')) return; const cr = c.getBoundingClientRect(); if (cr.height) maxB = Math.max(maxB, cr.bottom); });
    return [i + 1, Math.round(r.bottom - maxB)];
  }));
  console.log('folga inferior (px) por página:', JSON.stringify(over));
  await p.pdf({ path: 'PULSO_jornal_dos_enigmas.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
  const shots = process.argv.slice(2).map(Number);
  const pages = await p.$$('.page');
  for (const i of shots) await pages[i - 1].screenshot({ path: process.env.OUT + `/p${i}.png` });
  await b.close();
})();
