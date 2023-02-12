<template>
  <q-layout view="lHh Lpr lFf">
    <q-header
    id="header">
      <!-- <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />
      </q-toolbar> -->
      <!-- <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat+Alternates:wght@500&display=swap" rel="stylesheet">  -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat+Alternates:wght@500&family=Quicksand&display=swap" rel="stylesheet">


    <a href="/">
        <div id="title" class="text-h3">Summify</div>
        <div id="flavour" class="text-subtitle1">Condense your productivity</div>
      </a>
      <div id="blog-link"><a href="./#/blog">Development Blog</a></div>
      </q-header>

    <!-- <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <q-item-label
          header
        >
          Essential Links
        </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer> -->

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent } from "vue";
// import EssentialLink from 'components/EssentialLink.vue'

// const linksList = [
//   {
//     title: 'Docs',
//     caption: 'quasar.dev',
//     icon: 'school',
//     link: 'https://quasar.dev'
//   },
//   {
//     title: 'Github',
//     caption: 'github.com/quasarframework',
//     icon: 'code',
//     link: 'https://github.com/quasarframework'
//   },
//   {
//     title: 'Discord Chat Channel',
//     caption: 'chat.quasar.dev',
//     icon: 'chat',
//     link: 'https://chat.quasar.dev'
//   },
//   {
//     title: 'Forum',
//     caption: 'forum.quasar.dev',
//     icon: 'record_voice_over',
//     link: 'https://forum.quasar.dev'
//   },
//   {
//     title: 'Twitter',
//     caption: '@quasarframework',
//     icon: 'rss_feed',
//     link: 'https://twitter.quasar.dev'
//   },
//   {
//     title: 'Facebook',
//     caption: '@QuasarFramework',
//     icon: 'public',
//     link: 'https://facebook.quasar.dev'
//   },
//   {
//     title: 'Quasar Awesome',
//     caption: 'Community Quasar projects',
//     icon: 'favorite',
//     link: 'https://awesome.quasar.dev'
//   }
// ]
window.onscroll = scroll;

function scroll () {
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

  // components: {
  //   EssentialLink
  // },

  // setup () {
  //   const leftDrawerOpen = ref(false)

  //   return {
  //     essentialLinks: linksList,
  //     leftDrawerOpen,
  //     toggleLeftDrawer () {
  //       leftDrawerOpen.value = !leftDrawerOpen.value
  //     }
  //   }
  // }
});
</script>
