pip install -e.
cd src || exit 1

uvicorn main:app --reload --workers 2
