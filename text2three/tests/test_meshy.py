import argparse
from pathlib import Path 
from text2three.models.meshy import MeshyModel
from text2three.viewer import viewer

def main():
    parser = argparse.ArgumentParser(description="Test Meshy 3D generation")
    parser.add_argument(
        "-p", "--prompt",
        type=str,
        required=True,
        help="Text prompt to generate the 3D model"
    )
    args = parser.parse_args()

    print(f"==> Starting Meshy generation for prompt: {args.prompt}")
    
    output_dir = Path(__file__).parent.parent / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{args.prompt.replace(' ', '_')}.glb"

    model = MeshyModel()
    model.generate(args.prompt, output_path=output_path)

    print(f"✅ Model generated and saved to: {output_path}")

    viewer.launch_viewer(str(output_path))


if __name__ == "__main__":
    main()
