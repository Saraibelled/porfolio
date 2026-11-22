#!/usr/bin/env python3
"""
Rellena la columna `imagen` de piezas_porfolio.csv con la imagen de portada
de cada pieza (la etiqueta og:image, la misma que sale al compartirla en redes).

Uso (en la carpeta donde está el CSV):

    python3 actualizar_imagenes.py              # solo piezas del mar sin imagen o con imagen rota
    python3 actualizar_imagenes.py --todas      # todas las piezas del CSV, no solo las del mar
    python3 actualizar_imagenes.py --forzar     # vuelve a buscar la imagen aunque ya tengan una

No necesita instalar nada: solo Python 3.
Guarda una copia de seguridad como piezas_porfolio.backup.csv antes de escribir.
"""
import csv
import html
import re
import shutil
import sys
import time
import urllib.request
from urllib.parse import urljoin

CSV = "piezas_porfolio.csv"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
TODAS = "--todas" in sys.argv
FORZAR = "--forzar" in sys.argv


def si(v):
    return (v or "").strip().lower() in ("sí", "si", "x", "1", "true")


def pedir(url, metodo="GET"):
    req = urllib.request.Request(url, method=metodo, headers={"User-Agent": UA, "Accept-Language": "es-ES,es;q=0.9"})
    return urllib.request.urlopen(req, timeout=15)


def imagen_funciona(url):
    if not url:
        return False
    if url.startswith("//"):
        url = "https:" + url
    try:
        with pedir(url, "HEAD") as r:
            return r.status == 200
    except Exception:
        try:
            with pedir(url) as r:
                return r.status == 200
        except Exception:
            return False


def og_image(url):
    with pedir(url) as r:
        page = r.read(400_000).decode("utf-8", "ignore")
    for pat in (
        r'<meta[^>]+property=["\']og:image(?::secure_url)?["\'][^>]+content=["\']([^"\']+)',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']',
        r'<meta[^>]+name=["\']twitter:image["\'][^>]+content=["\']([^"\']+)',
    ):
        m = re.search(pat, page, re.I)
        if m:
            return urljoin(url, html.unescape(m.group(1)))
    return ""


def main():
    with open(CSV, encoding="utf-8-sig", newline="") as f:
        filas = list(csv.DictReader(f))
        campos = list(filas[0].keys())
    shutil.copy(CSV, CSV.replace(".csv", ".backup.csv"))

    revisar = [r for r in filas if (TODAS or si(r.get("en_el_mar"))) and r.get("url")]
    cambiadas = 0
    for i, r in enumerate(revisar, 1):
        actual = (r.get("imagen") or "").strip()
        if actual and not FORZAR and imagen_funciona(actual):
            continue
        try:
            nueva = og_image(r["url"])
        except Exception as e:
            print(f"[{i}/{len(revisar)}] ✗ no se pudo abrir la pieza: {r['titulo'][:60]} ({e})")
            continue
        if nueva and nueva != actual:
            r["imagen"] = nueva
            cambiadas += 1
            print(f"[{i}/{len(revisar)}] ✓ {r['titulo'][:60]}")
        else:
            print(f"[{i}/{len(revisar)}] · sin og:image: {r['titulo'][:60]}")
        time.sleep(0.4)

    with open(CSV, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)
    print(f"\nListo: {cambiadas} imágenes actualizadas en {CSV} (copia de seguridad en piezas_porfolio.backup.csv).")


if __name__ == "__main__":
    main()
