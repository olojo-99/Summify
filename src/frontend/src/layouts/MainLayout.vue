<template>
  <q-layout view="lHh Lpr lFf">
    <q-header id="header">
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Montserrat+Alternates:wght@500&family=Quicksand&display=swap"
        rel="stylesheet">


      <a href="/">
        <div id="title" class="text-h3">Summify</div>
        <div id="flavour" class="text-subtitle1">Condense your productivity</div>
      </a>
      <div id="blog-link"><a href="./#/blog">Development Blog</a></div>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent } from "vue";

// When the page is scrolled, run this
window.onscroll = scroll;

// Shrinks the header if user scrolls down, expands it if they scroll back up
function scroll() {
  let title = document.getElementById("title")
  let flavour = document.getElementById("flavour")
  let header = document.getElementById("header")
  // scrolling down
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    title.style.fontSize = "1.5em";
    title.style.paddingTop = "0.0em";
    title.style.paddingLeft = "0.2em";
    title.style.lineHeight = "1.5em";
    flavour.style.fontSize = "0em";
    flavour.style.opacity = "0.0";
    header.style.height = "2.5em";
  }
  // scrolling up
  else {
    header.style.height = "12em";
    title.style.fontSize = "10em";
    title.style.paddingTop = "0.32em";
    title.style.lineHeight = "3.125rem";
    title.style.paddingLeft = "0.2em";
    flavour.style.fontSize = "2em";
    flavour.style.opacity = "0.7";
  }
}

export default defineComponent({
  name: "MainLayout",
});
</script>
