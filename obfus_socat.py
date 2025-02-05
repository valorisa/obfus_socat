#!/usr/bin/env python3

import argparse
import subprocess
import os

def run_socat(args):
    """Construit et exécute la commande socat."""
    socat_cmd = ["socat"]

    if args.mode == "ssl":
        socat_cmd += [
            f"OPENSSL-LISTEN:{args.local_port},cert={args.cert_path},key={args.key_path},reuseaddr,fork",
            f"OPENSSL:{args.remote_host}:{args.remote_port},verify=0"
        ]
    elif args.mode == "ssh":
        socat_cmd += [
            f"TCP-LISTEN:{args.local_port},reuseaddr,fork",
            f"EXEC:'ssh -T {args.remote_host} socat - TCP:{args.remote_port}'"
        ]

    if args.daemon:
        socat_cmd.insert(0, "nohup")
        socat_cmd.append("&")

    print(f"Exécution de : {' '.join(socat_cmd)}")
    subprocess.run(" ".join(socat_cmd), shell=True)

def main():
    parser = argparse.ArgumentParser(description="Obfus Socat - Tunnel sécurisé avec socat")
    
    parser.add_argument("mode", choices=["ssl", "ssh"], help="Mode de connexion : ssl ou ssh")
    parser.add_argument("--local_port", type=int, required=True, help="Port local à écouter")
    parser.add_argument("--remote_host", type=str, required=True, help="Hôte distant")
    parser.add_argument("--remote_port", type=int, required=True, help="Port distant")
    parser.add_argument("--cert_path", type=str, default="config/server.crt", help="Chemin du certificat SSL")
    parser.add_argument("--key_path", type=str, default="config/server.key", help="Chemin de la clé privée SSL")
    parser.add_argument("--daemon", action="store_true", help="Exécuter en arrière-plan")

    args = parser.parse_args()
    run_socat(args)

if __name__ == "__main__":
    main()

