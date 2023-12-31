import os.path
from system import relative
from fastapi.responses import HTMLResponse

def get_redoc_html(
		*,
		openapi_url: str,
		title: str,
		redoc_favicon_url: str = "https://cdn.worldvectorlogo.com/logos/fastapi-1.svg",
		with_google_fonts: bool = True,
) -> HTMLResponse:
	html = f"""<!DOCTYPE html><html><head><title>{title}</title><!-- needed for adaptive design --><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1">"""
	if with_google_fonts:
		html += """<link href="https://fonts.googleapis.com/css?family=Inter:300,400,700|Inter:300,400,700" rel="stylesheet">"""
		html += f"""<link rel="shortcut icon" href="{redoc_favicon_url}">
			</head> 
			<body>
			<div id="redoc-container">

			</div>
			<script src="https://cdn.jsdelivr.net/npm/redoc@2.0.0-rc.55/bundles/redoc.standalone.js"></script>
			<script src="/static/docs/try.js"></script>
			<script>	
			initTry({{
			openApi: `{openapi_url}`,
			redocOptions: {{scrollYOffset: 0, disableSidebar: false}},
			}})
			</script>
			<script src="/static/docs/adapt.js"></script>
			<link rel="stylesheet" href="/static/docs/try.css">
			<link rel="stylesheet" href="/static/docs/style.css">
			</body></html>
			"""

	return HTMLResponse(html)
