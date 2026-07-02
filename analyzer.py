import tarfile
import re

def analisar_sysdiagnose(arquivo):
    achados = []

    with tarfile.open(arquivo, "r:*") as tar:
        for m in tar.getmembers():
            if m.isfile():
                f = tar.extractfile(m)
                if not f:
                    continue

                texto = f.read().decode(errors="ignore")

                if re.search(r"proxy", texto, re.I):
                    achados.append(f"Proxy encontrado em {m.name}")

                if re.search(r"vpn", texto, re.I):
                    achados.append(f"VPN encontrado em {m.name}")

                if re.search(r"dns", texto, re.I):
                    achados.append(f"DNS encontrado em {m.name}")

                if re.search(r"network|socket|connection", texto, re.I):
                    achados.append(f"Rede encontrada em {m.name}")

    return achados
