/* file which waits for the window to load then plays an animation */

/* HELPER FUNCTIONS */

const hue = 1;
function css(elements, style) {
  for (var i = 0; i < elements.length; i++) {
    for (const property in style) elements[i].style[property] = style[property];
  }
}

const randomColor = (hue) =>
  `rgb(${hue ? hue : Math.floor(Math.random() * 255)}, ${Math.floor(
    Math.random() * 255
  )}, ${Math.floor(Math.random() * 255)})`;

function backgroundBody(color) {
  const parent = document.querySelector("body");
  css([parent], {
    "background-color": color,
  });
}

function fancyLoadAnimation() {
  var w = window.innerWidth;
  var h = window.innerHeight;
  var numberOfStrips = 50;
  var animationWait = 1000;
  var stripH = h / numberOfStrips;

  const parent = document.querySelector("#fancy");

  css([parent], {
    position: "fixed",
    "z-index": 100,
    top: 0,
    left: 0,
    width: `${window.innerWidth}px`,
    height: `${window.innerHeight}px`,
  });

  setInterval(() => {}, animationWait);
  /*create Strips */
  for (var i = 0; i <= numberOfStrips; i++) {
    const stripContainer = document.createElement("div");

    css([stripContainer], {
      height: `${stripH}px`,
      padding: 0,
      margin: 0,
      display: "flex",
      "flex-direction": "row",
      width: `${window.innerWidth}px`,
    });

    const stripLeft = document.createElement("div");
    stripLeft.classList = ["strip"];
    stripContainer.appendChild(stripLeft);

    const stripRight = document.createElement("div");
    stripRight.classList = ["strip"];
    stripContainer.appendChild(stripRight);

    const sec = 4;

    css([stripLeft, stripRight], {
      "background-color": randomColor(hue),
      height: `${stripH}px`,
      padding: 0,
      margin: 0,
      position: "relative",
      width: `${window.innerWidth / 2}px`,
    });

    // set animation for horizontal strips LEFT
    setTimeout(() => {
      css([stripLeft], {
        "-webkit-animation-name": `runLeft`,
        "-webkit-animation": `runLeft ${
          sec * (1 + Math.random(3))
        }s normal forwards`,
        "-moz-animation": `runLeft ${
          sec * (1 + Math.random(3))
        }s normal forwards`,
        "-o-animation": `runLeft ${
          sec * (1 + Math.random(3))
        }s normal forwards`,
      });

      // set animation for horizontal strips RIGHT
      css([stripRight], {
        "-webkit-animation-name": "runRight",
        "-webkit-animation": `runRight ${
          sec * (1 + Math.random(3))
        }s normal forwards`,
        "-moz-animation": `runRight  ${
          sec * (1 + Math.random(3))
        }s normal forwards`,
        "-o-animation": `runRight  ${
          sec * (1 + Math.random(3))
        }s normal forwards`,
        width: `${window.innerWidth / 2}px`,
      });
    }, animationWait);

    // black fade in
    setTimeout(() => {
      css([parent], {
        "-webkit-animation": `fade ${sec}s normal forwards`,
        "-moz-animation": `fade  ${sec}s normal forwards`,
        "-o-animation": `fade ${sec}s normal forwards`,
      });
    }, animationWait);

    // remove animation container
    setTimeout(() => {
      document.querySelector("#fancy").remove(sec);
    }, animationWait + 5000);

    parent.appendChild(stripContainer);
  }
}

/* ------------------MAIN PROGRAM --------------------------------*/

function init() {
  console.log("page has loaded");
  fancyLoadAnimation();
  backgroundBody("#407076");
}

// wait for window to load then start program
window.addEventListener("load", (event) => {
  console.log("page is fully loaded, add your scripts here");
  init();
});
