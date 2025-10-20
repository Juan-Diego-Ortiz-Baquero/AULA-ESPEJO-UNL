function menuToggle() {
  var nav = document.getElementById("nav");
  var toggle = document.getElementById("toggle");
  nav.classList.toggle("hidden");
  toggle.classList.toggle("active");
}

// Sidebar menu functionality
$(document).ready(function() {
  // Menu toggle functions
  $("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
  });
  
  $("#menu-toggle-2").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled-2");
    $("#menu ul").hide();
  });

  // Initialize collapsible menu
  function initMenu() {
    $("#menu ul").hide();
    $("#menu ul").children(".current").parent().show();
    $("#menu li a").click(function() {
      var checkElement = $(this).next();
      if (checkElement.is("ul") && checkElement.is(":visible")) {
        return false;
      }
      if (checkElement.is("ul") && !checkElement.is(":visible")) {
        $("#menu ul:visible").slideUp("normal");
        checkElement.slideDown("normal");
        return false;
      }
    });
  }
  
  initMenu();
});

// Asegurar que el menú esté oculto al cargar la página
window.onload = function() {
  var nav = document.getElementById("nav");
  var toggle = document.getElementById("toggle");
  
  // Asegurar que el menú esté oculto
  nav.classList.add("hidden");
  
  // Asegurar que el botón muestre el icono de hamburguesa
  toggle.classList.remove("active");
};