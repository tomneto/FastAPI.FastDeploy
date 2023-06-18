import os.path

from fastapi.responses import HTMLResponse

with open(os.path.join(os.path.dirname(__file__) , "style.css"), "r") as css_file:
	css_content = css_file.read()


def get_redoc_html(
		*,
		openapi_url: str,
		title: str,
		redoc_favicon_url: str = "https://fastapi.tiangolo.com/img/favicon.png",
		with_google_fonts: bool = True,
) -> HTMLResponse:
	html = f"""<!DOCTYPE html><html><head><title>{title}</title><!-- needed for adaptive design --><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1">"""
	if with_google_fonts:
		html += """<link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">"""
		html += f"""<link rel="shortcut icon" href="{redoc_favicon_url}">
			</head> 
			<body>
			<div id="redoc-container"></div>
			<script src="https://cdn.jsdelivr.net/npm/redoc@2.0.0-rc.55/bundles/redoc.standalone.min.js"> </script>
			<script src="https://cdn.jsdelivr.net/gh/wll8/redoc-try@1.4.1/dist/try.js"></script>
			<script>	
			initTry({{
			openApi: `{openapi_url}`,
			redocOptions: {{scrollYOffset: 0, disableSidebar: true}},
			}})
			</script>
			"""

		html += """
				<script> 
function applySwaggerStyle() {
var swaggerBoxes = document.querySelectorAll('div[class^="opblock opblock-"]');
swaggerBoxes.forEach((box) => {
box.style.border = "0px solid";
box.style.color = "white";
});
var methodPlaceHolders = document.querySelectorAll('span[class^="sc-jHcXXw"]');
methodPlaceHolders.forEach((placeHolder) => {
let placeHolderStyle = placeHolder.style 
placeHolder.addEventListener('click', function() {
var tryButton = document.querySelectorAll('button[class^="tryBtn"]');
tryBtn.
});
});
};

setTimeout(function () {
applySwaggerStyle();
}, 3000);
</script>"""
		html += f""""<style>{css_content}</style></body></html>"""

	return HTMLResponse(html)
