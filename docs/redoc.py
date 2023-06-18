import os.path

from fastapi.responses import HTMLResponse

with open(os.path.join(os.path.dirname(__file__) , "style.css"), "r") as css_file:
	css_content = css_file.read()

def get_redoc_html(
		*,
		openapi_url: str,
		title: str,
		redoc_favicon_url: str = "https://cdn.worldvectorlogo.com/logos/fastapi-1.svg",
		with_google_fonts: bool = True,
) -> HTMLResponse:
	html = f"""<!DOCTYPE html><html><head><title>{title}</title><!-- needed for adaptive design --><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1">"""
	if with_google_fonts:
		html += """<link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">"""
		html += f"""<link rel="shortcut icon" href="{redoc_favicon_url}">
			</head> 
			<body>
			<div id="redoc-container">

			</div>
			
			<script src="https://cdn.jsdelivr.net/npm/redoc@2.0.0-rc.55/bundles/redoc.standalone.js"> </script>
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
var tables = document.querySelectorAll("table")
tables.forEach(table => {
    table.setAttribute("hidden", "hidden")
});
var tables = document.querySelectorAll("table");
var tablesPlaceHolders = document.querySelectorAll("h5");

tables.forEach(function(table, index) {
  table.setAttribute("aria-expanded", "false");
  tablesPlaceHolders[index].style.textTransform = "capitalize";
  tablesPlaceHolders[index].style.cursor = "pointer";
  tablesPlaceHolders[index].addEventListener("click", function() {
    table.toggleAttribute("hidden");

  });
  
  var validationErrorButtons = document.querySelectorAll("button[class^='sc-jXcxbT jsdzMI']");
validationErrorButtons.forEach(function(button) {
button.setAttribute("aria-expanded", "false");
  button.addEventListener("click", function() {
    var toggleState = button.getAttribute("aria-expanded");
    
    button.style.transition = "border-radius 0.4s linear";

    if (toggleState === "false") {
    	button.style.borderRadius = "0px";
      button.style.borderTopLeftRadius = "15px";
      button.style.borderTopRightRadius = "15px";
      button.style.borderBottomLeftRadius = "0px";
      button.style.borderBottomRightRadius = "0px";
    } else {
    button.style.borderRadius = "0px";
      button.style.borderTopLeftRadius = "0px";
      button.style.borderTopRightRadius = "0px";
      button.style.borderBottomLeftRadius = "15px";
      button.style.borderBottomRightRadius = "15px";
    }
  });
});

});
const container = document.querySelector('.sc-hKFxyN.gHYYBK.api-info');

const vercelLogo = document.createElement('img');
vercelLogo.src = 'https://assets.vercel.com/image/upload/v1588805858/repositories/vercel/logo.png';
vercelLogo.alt = 'vercelLogo';
vercelLogo.height = '100';

const fastApiLogo = document.createElement('img');
fastApiLogo.src = 'https://cdn.worldvectorlogo.com/logos/fastapi-1.svg';
fastApiLogo.alt = 'vercelLogo';
fastApiLogo.height = '100';

const dockerLogo = document.createElement('img');
dockerLogo.src = 'https://www.svgrepo.com/show/331370/docker.svg';
dockerLogo.alt = 'vercelLogo';
dockerLogo.height = '100';

const firstChild = container.firstChild;
container.insertBefore(fastApiLogo, firstChild);

/*container.insertBefore(vercelLogo, firstChild);
container.insertBefore(dockerLogo, firstChild);*/

};


setTimeout(function () {
applySwaggerStyle();
}, 1000);
</script>"""
		html += f""""<style>{css_content}</style></body></html>"""

	return HTMLResponse(html)
