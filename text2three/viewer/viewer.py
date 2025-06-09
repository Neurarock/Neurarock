def launch_viewer(glb_path: str, server_port: int = 8000):
    from pathlib import Path
    import subprocess
    import webbrowser
    import time

    glb_path = Path(glb_path).resolve()
    serve_dir = glb_path.parent

    print(f"📂 Serving from: {serve_dir}")

    proc = subprocess.Popen(
        ["python3", "-m", "http.server", str(server_port)],
        cwd=str(serve_dir),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    time.sleep(1)  # Give server a second to start

    url = f"http://localhost:{server_port}/viewer.html?model={glb_path.name}"
    print(f"🔍 Opening model preview at: {url}")
    webbrowser.open(url)

    try:
        print("📡 Server running... Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user.")
    finally:
        proc.terminate()
