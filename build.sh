set -e

echo "==> Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "==> Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "==> Cleaning previous build..."
rm -rf public

echo "==> Initializing Reflex..."
reflex init

echo "==> Exporting frontend..."
reflex export --frontend-only

echo "==> Unzipping output..."
unzip frontend.zip -d public
rm -f frontend.zip

echo "==> Build complete. Contents of public/:"
ls public/

deactivate
