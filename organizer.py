import argparse
import pathlib
import json
import logging
import sys
import shutil

from tqdm import tqdm


def load_configuration(config_path: pathlib.Path) -> dict:
    try:
        with open(config_path, "r") as config_file:
            config_data = json.load(config_file)
            return config_data
    except FileNotFoundError:
        logging.error(f'Config File: "{config_path}" does NOT EXIST.')
        logging.error(
            "Please make sure 'config.json' exists in the same directory as the script."
        )
        sys.exit(1)
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing config file: {config_path}")
        logging.error(f"Invalid Json! Please fix 'config.json'. {e}")
        sys.exit(1)


def process_files(
    file_path: pathlib.Path,
    file_path_map: dict,
    source_path: pathlib.Path,
    dry_run: bool,
):
    file_extension = file_path.suffix.lower()
    destination_folder_name = "Other"

    for document_type, extensions in file_path_map.items():
        if file_extension in extensions:
            destination_folder_name = document_type
            break

    designated_dir = source_path / destination_folder_name

    if dry_run:
        designated_file_path = designated_dir / file_path.name
        logging.info(f"[DRY-RUN] Would move {file_path.name} to {designated_file_path}")
    else:
        designated_dir.mkdir(exist_ok=True, parents=True)

        designated_file_path = designated_dir / file_path.name
        counter: int = 1
        while designated_file_path.exists():
            logging.warning(
                f"Conflict: File Already Exist. File: {designated_file_path}"
            )
            new_file_name = f"{file_path.stem}_({counter}){file_extension}"
            designated_file_path = designated_dir / new_file_name
            counter += 1

        try:
            shutil.move(file_path, designated_file_path)
            logging.info(f"Moved: {file_path.name} into {designated_file_path}")
        except PermissionError as e:
            logging.error(f"Could not move {file_path.name}. ERROR: {e}")
        except Exception as e:
            logging.error(f"An unexpected error ocored. ERROR: {e}")


def organize_directory(source_path: pathlib.Path, dry_run: bool, file_path_map: dict):
    logging.info(f"Organizing File of -> {source_path}")

    if dry_run:
        logging.info("--- DRY RUN MODE ENABLED: No files will be moved. ---")
    else:
        logging.info("--- LIVE RUN MODE ENABLED: File system changes will be made. ---")

    file_to_process = [item for item in source_path.iterdir() if item.is_file()]

    for file_item in tqdm(file_to_process, desc="Organizing Files"):
        process_files(file_item, file_path_map, source_path, dry_run)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by their type.",
        epilog="Example: python organizer.py /path/to/downloads",
    )
    parser.add_argument(
        "source_directory", help="The path of the directory you wanna organize."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate the orgnaization without moving the file.",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("organizer.log"),
            logging.StreamHandler(sys.stdout),
        ],
    )

    config_file_path = pathlib.Path(__file__).parent / "config.json"

    file_type_config_map = load_configuration(config_file_path)

    source_path = pathlib.Path(args.source_directory).expanduser()

    if not source_path.exists() or not source_path.is_dir():
        logging.error(
            f"ERROR: {source_path} Path does not Exist or is not a Directory."
        )
        sys.exit(1)

    organize_directory(source_path, args.dry_run, file_type_config_map)
