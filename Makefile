.PHONY: help refresh-portfolio-metrics public-export public-serve public-check public-publish-gh-pages

help:
	@echo "Targets:"
	@echo "  refresh-portfolio-metrics   Sync PORTFOLIO.md metrics from today.md"
	@echo "  public-export               Build the publishable public/ bundle"
	@echo "  public-serve                Serve public/ locally at http://localhost:8000"
	@echo "  public-check                Quick scan public/ for obvious secret patterns"
	@echo "  public-publish-gh-pages      Commit public/ into gh-pages branch (set PUBLISH=1; push with PUSH=1)"

refresh-portfolio-metrics:
	python3 tools/refresh-portfolio-metrics.py

public-export:
	python3 tools/public-export.py

public-serve:
	cd public && python3 -m http.server 8000

public-check:
	cd public && rg -n "(sk-|sk_|api[_-]?key|secret|bearer\\s+|authorization:|token|password)" -S . || true

public-publish-gh-pages:
	bash tools/public-publish-gh-pages.sh
