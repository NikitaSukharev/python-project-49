install:
	uv sync

lint:
	uv run ruff check brain_games

build:
	rm -rf dist
	uv build

release:
	rm -rf dist
	uv version patch
	uv build
	uv pip install --force-reinstall dist/*.whl

package-install:
	uv tool install dist/*.whl

clean:
	rm -rf dist .venv *.egg-info

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime