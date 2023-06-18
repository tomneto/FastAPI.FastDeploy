function applySwaggerStyle() {
  var swaggerBoxes = document.querySelectorAll(
    'div[class^="opblock opblock-"]'
  );
  swaggerBoxes.forEach((box) => {
    box.style.border = "0px solid";
    box.style.color = "white";
  });
  var tables = document.querySelectorAll("table");
  tables.forEach((table) => {
    table.setAttribute("hidden", "hidden");

  });
  var tables = document.querySelectorAll("table");
  var tablesPlaceHolders = document.querySelectorAll("h5");

  tables.forEach(function (table, index) {
    table.setAttribute("aria-expanded", "false");
    tablesPlaceHolders[index].style.borderRadius = "15px";
    tablesPlaceHolders[index].style.textTransform = "capitalize";
    tablesPlaceHolders[index].style.transition = "border-radius 0.4s linear";
    tablesPlaceHolders[index].style.cursor = "pointer";
    tablesPlaceHolders[index].addEventListener("click", function () {
      table.toggleAttribute("hidden");
      
      var toggleState = table.getAttribute("aria-expanded");
      if (toggleState === "true") {
        tablesPlaceHolders[index].style.borderTopLeftRadius = "15px";
        tablesPlaceHolders[index].style.borderTopRightRadius = "15px";
        tablesPlaceHolders[index].style.borderBottomLeftRadius = "15px";
        tablesPlaceHolders[index].style.borderBottomRightRadius = "15px";
        table.setAttribute("aria-expanded", "false");
      } else {
        tablesPlaceHolders[index].style.borderTopLeftRadius = "15px";
        tablesPlaceHolders[index].style.borderTopRightRadius = "15px";
        tablesPlaceHolders[index].style.borderBottomLeftRadius = "0px";
        tablesPlaceHolders[index].style.borderBottomRightRadius = "0px";
        table.setAttribute("aria-expanded", "true");
      }

    });
  });

  var validationErrorButtons = document.querySelectorAll(
    "button[class^='sc-jXcxbT jsdzMI']"
  );
  validationErrorButtons.forEach(function (button) {
    button.setAttribute("aria-expanded", "false");
    button.addEventListener("click", function () {
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

  const container = document.querySelector(".sc-hKFxyN.gHYYBK.api-info");

  const vercelLogo = document.createElement("img");
  vercelLogo.src =
    "https://assets.vercel.com/image/upload/v1588805858/repositories/vercel/logo.png";
  vercelLogo.alt = "vercelLogo";
  vercelLogo.height = "100";

  const fastApiLogo = document.createElement("img");
  fastApiLogo.src = "https://cdn.worldvectorlogo.com/logos/fastapi-1.svg";
  fastApiLogo.alt = "vercelLogo";
  fastApiLogo.height = "100";

  const dockerLogo = document.createElement("img");
  dockerLogo.src = "https://www.svgrepo.com/show/331370/docker.svg";
  dockerLogo.alt = "vercelLogo";
  dockerLogo.height = "100";

  const firstChild = container.firstChild;
  container.insertBefore(fastApiLogo, firstChild);

  /*container.insertBefore(vercelLogo, firstChild);
  container.insertBefore(dockerLogo, firstChild);*/
}

setTimeout(function () {
  applySwaggerStyle();
}, 1000);
