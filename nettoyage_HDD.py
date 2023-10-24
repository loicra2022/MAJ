import os
import shutil

def cleanup_disk_space(target_folder, max_usage_percent):
    total, used, free = shutil.disk_usage(target_folder)
    current_usage_percent = (used / total) * 100

    if current_usage_percent < max_usage_percent:
        print(f"Disk space is currently at {current_usage_percent}%. No action required.")
        return

    print(f"Disk space is currently at {current_usage_percent}%. Cleaning up...")

    for root, dirs, files in os.walk(target_folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"Deleted {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

if __name__ == "__main__":
    target_folder = "/path/to/target/folder"  # Remplacez ceci par le chemin du dossier cible
    max_usage_percent = 80  # Réglez ceci sur le pourcentage d'utilisation maximal souhaité

    cleanup_disk_space(target_folder, max_usage_percent)
