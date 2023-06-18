from fastapi.responses import HTMLResponse


def get_redoc_html(
		*,
		openapi_url: str,
		title: str,
		redoc_favicon_url: str = "https://fastapi.tiangolo.com/img/favicon.png",
		with_google_fonts: bool = True,
) -> HTMLResponse:
	html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>{title}</title>
    <!-- needed for adaptive design -->
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    """
	if with_google_fonts:
		html += """
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">
    """
	html += f"""
        <link rel="shortcut icon" href="{redoc_favicon_url}">
        <!--
        ReDoc doesn't change outer page styles
        -->
        <style>
          body {{
            margin: 0;
            padding: 0;
          }}

          button.tryBtn {{
          	font-family: Inter;
            display: inline-block;
            padding: 10px 10px;
            margin-right: 10px;
            left-padding: 5px;
            font-size: 12px;
            font-weight: bold;
            text-align: center;
            text-decoration: none;
            color: #ffffff;
            background-color: #007bff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            }}


		button.tryBtn:hover {{
		  background-color: #0056b3;
		}}

		button.tryBtn:active {{
		  background-color: #003d80;
		}}
        </style>
        </head>
        <body>
            <div id="redoc-container"></div>
              <script src="https://cdn.jsdelivr.net/npm/redoc@2.0.0-rc.55/bundles/redoc.standalone.min.js"> </script>
              <script src="https://cdn.jsdelivr.net/gh/wll8/redoc-try@1.4.1/dist/try.js"></script>
              <script>
                initTry({{
                openApi: `{openapi_url}`,
                  redocOptions: {{scrollYOffset: 50}},
                }})
              </script>
        </body>
        </html>
        """
	return HTMLResponse(html)
