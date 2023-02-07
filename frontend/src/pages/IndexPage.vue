<template>
  <q-page
    id="main-container"
    class="flex">

    <div
      v-if="sum == false"
      id="search-container"
      class="flex flex-center flex-item column">

      <div
        id="description"
        class="flex-item">
        <p>Summify is a free study tool.</p>
        <p>Enter a Youtube video link and click submit to generate a summarised transcript.</p>
        <p>Videos that do not have captions or have captions turned off by the author will not work.</p>
      </div>

      <div
        id="search-bar"
        class="flex-item">
        <q-form
          ref="formComponent"
          @submit.prevent>
          <div id="bar-button">
          <q-input
            v-model="id"
            error-message="Please enter a valid Youtube video"
            name="id"
            filled
            type="url"
            outlined
            label="Insert Video URL"
            for="link-input"
          />
          <q-ajax-bar
            id="ajax"
            ref="bar"
            position="bottom"
            color="accent"
            size="20px"
          />
          <q-btn
            @click="onSubmit"
            id="submit-button"
            label="Submit"
            type="submit"
            color="primary" />
            </div>
        </q-form>
      </div>
    </div>

    <div
      v-else
      id="content"
      class="flex row">

      <!-- left column -->
      <div
        id="left"
        class="flex-item">
        <div id="video-embed">
          <iframe
            width="560"
            height="315"
            v-bind:src="embed_id(get_id(id))"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen></iframe>
        </div>


        <div v-if="links_ready == false" id="right"
          class="flex-items">
          <q-spinner color="accent"
            size="10em"/>
            <h5 class="text-h5">Retrieving information from summary: Generating links</h5>


    </div>
      <div
      v-else
        id="links"
        >
        <div id="link-container" class="flex column">


<a v-for="link in links" v-bind:key="link"
:href="link.URL"
target="_blank"
class="flex">
<q-card
class="q-pt-none"
flat
square
>
<!-- <q-separator inset /> -->
<q-card-section horizontal>
<q-card-section>
  <img :src="link.icon" width="16" height="16">
</q-card-section>
<q-card-section>
  {{ link.title }}
</q-card-section>
</q-card-section>
<!-- <q-separator inset /> -->
</q-card>
</a>
          
<!-- <a
id="link1"
v-bind:href="link1"
target="_blank">
          <q-card
            class="q-pt-none"
            flat
            bordered
            square>
            <q-card-section>
              <q-img src="https://picsum.photos/100/100"></q-img>
            </q-card-section>

            <q-card-section>
              {{  link1  }}
            </q-card-section>
          </q-card>

</a>

<a
id="link2"
v-bind:href="link2"
target="_blank">
          <q-card
            class="q-pt-none"
            flat
            bordered
            square>
            <q-card-section>
              <q-img src="https://picsum.photos/100/100"></q-img>
            </q-card-section>

            <q-card-section>
              {{  link2  }}
            </q-card-section>
          </q-card>
</a> -->

        </div>
      </div>
      </div>

      <!-- middle column -->
      <div
        id="middle"
        class="flex-item">

        <div id="transcript-text">
          <h2>General Summary:</h2>
          <p
            id="summary-body"
            class="text-body1">{{ text }}
          </p>

          <h2>5 Minute Segments:</h2>


            <div id="sub-summaries" class="text-body1">
              <div v-for="(value, key) in subs"  v-bind:key="key" class="sub-summary">
                <span class="timestamp">{{ key }}: </span>{{ value }}
              </div>
            </div>



        </div>

      </div>

      <!-- right column -->
      
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import axios, { api } from 'boot/axios'
import {Loading, Notify, QSpinnerGears, LoadingBar} from 'quasar'

// LoadingBar.setDefaults({
//   color: 'amber',
//   size: '15px',
//   position: 'bottom',
//   increment: '10'
// })


    const refComponent = ref(null)
    const id = ref(null)
    var summary = ref(null);
    var links = ref(null);
    var subs = ref(null)
    var URL_BASE = "http://127.0.0.1:5000"
    const summary_ready = ref(false);
    const links_ready = ref(false)


    // window.onload = init;
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
        title.style.paddingLeft = "0em";
        flavour.style.fontSize = "2em";
        flavour.style.opacity = "0.7";
      }
    }



const getData = async id => {
              
              try {
                Loading.show({
                message: "Generating summary",
                backgroundColor: "black",
                customClass: "loading",
                spinnerColor: "white",
                messageColor: "white",
                boxClass: "bg-amber text-white"
              })
                console.log(id)
                const response = await api.get(URL_BASE + "/summarise/" + id)
                console.log(response)
                const data = response.data
                console.log(data)

                console.log(data.sub)
                summary.value = data.overall

                subs.value = data.segments
                console.log(subs.value)
                summary_ready.value = true;
                // insertSubs(data.text.sub)
                Loading.hide()

                console.log('getting links')
                const response2 = await api.get(URL_BASE + "/links/" + id)
                console.log(response)
                const data2 = response2.data
                links.value = data2.links
                links_ready.value = true;


                
              }
              catch (error) {
                console.log("REEEEEEE")
                Notify.create("The request has failed. i'm truly sorry.")
                Loading.hide()
              }
                  // Loading.hide()
            }



// const getLinks = async id => {
//       console.log('getting links')
//       const response = await api.get(URL_BASE + "/links/" + id)
//       console.log(response)
//       const data = response.data
//       link1.value = data.IR[0]
//       link2.value = data.IR[1]
//       links_ready.value = true;
//     }

export default {
  setup() {

    const bar = ref(null)

          function get_id(url_link) {
            if (url_link.includes("youtube")) {
              // full url
              let last_slash = url_link.lastIndexOf("v=")
              return url_link.slice(last_slash + 2)
            }
            else if (url_link.includes("youtu.be")) {
              let last_slash = url_link.lastIndexOf("/")
              return url_link.slice(last_slash)
            }
            else {
              return false
            }
          }

          function embed_id(vid_id) {
            return "https://www.youtube.com/embed/" + vid_id
          }


          // function trigger() {
          //   const barRef = bar.value
          //   barRef.start()

          //   setTimeout(() => {
          //     const barRef = bar.value
          //     if (barRef) {
          //       barRef.stop()
          //     }
          //   }, Math.random() * 3000 + 1000)
          // }




    return {
      id,
      bar,
      subs,
      // trigger,
      get_id,
      embed_id,
      sum: summary_ready,
      text: summary,
      // link1: link1,
      // link2: link2,
      links,
      links_ready,

      onSubmit() {
        console.log("submit button pressed")
        const vid_id = get_id(id.value)
        if (vid_id) {
          // trigger()
          getData(vid_id)
          // getLinks(vid_id)
          
        }
        else {
          // error handling here
        }
      }



    };
  }
};

</script>
