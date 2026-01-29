#!/usr/bin/env python3
"""
ProCAST AI Automation Presentation - Web Application
Serves presentation slides, dashboard mockup, and ROI calculator
"""

from __future__ import annotations

import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

APP_NAME = "ProCAST AI Automation"


def _root_path() -> str:
    root_path = os.getenv("ROOT_PATH", "").strip()
    if not root_path:
        return ""
    if not root_path.startswith("/"):
        root_path = f"/{root_path}"
    return root_path.rstrip("/")


def create_app() -> FastAPI:
    root_path = _root_path()
    app = FastAPI(title=APP_NAME, root_path=root_path)

    app.add_middleware(
        SessionMiddleware,
        secret_key="procast-presentation-secret-key-change-in-production",
        same_site="lax",
        https_only=False,
    )

    # Get the directory where this file is located
    app_dir = Path(__file__).parent.parent
    static_dir = app_dir / "static"
    templates_dir = app_dir / "templates"

    # Create directories if they don't exist
    static_dir.mkdir(exist_ok=True)
    templates_dir.mkdir(exist_ok=True)

    # Mount static files
    if static_dir.exists():
        app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

    # Setup templates
    templates = Jinja2Templates(directory=str(templates_dir))

    @app.get("/", response_class=HTMLResponse)
    async def home(request: Request):
        """Main landing page"""
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "page_title": "ProCAST AI Automation - Home",
            }
        )

    @app.get("/presentation", response_class=HTMLResponse)
    async def presentation(request: Request):
        """Main presentation slides"""
        return FileResponse(
            app_dir / "presentation-slides.html",
            media_type="text/html"
        )

    @app.get("/dashboard", response_class=HTMLResponse)
    async def dashboard(request: Request):
        """Interactive dashboard mockup"""
        return FileResponse(
            app_dir / "dashboard-mockup.html",
            media_type="text/html"
        )

    @app.get("/roi-calculator", response_class=HTMLResponse)
    async def roi_calculator(request: Request):
        """ROI Calculator"""
        return FileResponse(
            app_dir / "roi-calculator.html",
            media_type="text/html"
        )

    @app.get("/demo-script", response_class=HTMLResponse)
    async def demo_script(request: Request):
        """Demo script and guide"""
        demo_script_file = app_dir / "demo-script.md"
        if demo_script_file.exists():
            with open(demo_script_file, 'r') as f:
                content = f.read()
        else:
            content = "Demo script not found"

        return templates.TemplateResponse(
            "markdown.html",
            {
                "request": request,
                "page_title": "Demo Script",
                "content": content,
            }
        )

    @app.get("/technical-architecture", response_class=HTMLResponse)
    async def technical_architecture(request: Request):
        """Technical architecture documentation"""
        tech_file = app_dir / "technical-architecture.md"
        if tech_file.exists():
            with open(tech_file, 'r') as f:
                content = f.read()
        else:
            content = "Technical architecture document not found"

        return templates.TemplateResponse(
            "markdown.html",
            {
                "request": request,
                "page_title": "Technical Architecture",
                "content": content,
            }
        )

    @app.get("/presentation-guide", response_class=HTMLResponse)
    async def presentation_guide(request: Request):
        """Presentation delivery guide"""
        guide_file = app_dir / "presentation-guide.md"
        if guide_file.exists():
            with open(guide_file, 'r') as f:
                content = f.read()
        else:
            content = "Presentation guide not found"

        return templates.TemplateResponse(
            "markdown.html",
            {
                "request": request,
                "page_title": "Presentation Guide",
                "content": content,
            }
        )

    @app.get("/outline", response_class=HTMLResponse)
    async def outline(request: Request):
        """Presentation outline"""
        outline_file = app_dir / "presentation-outline.md"
        if outline_file.exists():
            with open(outline_file, 'r') as f:
                content = f.read()
        else:
            content = "Outline not found"

        return templates.TemplateResponse(
            "markdown.html",
            {
                "request": request,
                "page_title": "Presentation Outline",
                "content": content,
            }
        )

    return app


# Create app instance
app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
