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
      </div>

      <!-- middle column -->
      <div
        id="middle"
        class="flex-item">

        <div id="transcript-text">
          <h1 class="text-h1">Summary</h1>
          <h2>General:</h2>
          <p
            id="summary-body"
            class="text-body1">{{ text }}
          </p>

          <h2>5 Minute Segments:</h2>


            <div id="sub-summaries" class="text-body1">
              <div v-for="(value, key) in subs"  v-bind:key="key">
                <span class="timestamp">{{ key }}: </span>{{ value }}
              </div>
            </div>



        </div>

      </div>

      <!-- right column -->
      <div v-if="links == false" id="right"
      class="flex-items">
      <q-spinner color="accent"
        size="10em"/>
        <h5 class="text-h5">Retrieving information from summary: Generating links</h5>


    </div>
      <div
      v-else
        id="right"
        class="flex-item">
        <div id="links">
<a
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
</a>

        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import axios, { api } from 'boot/axios'
import {Loading, Notify} from 'quasar'

// function init() {
    //   var button = document.getElementById('submit-button');
    //   button.addEventListener("click", switchState);
    // }

    const refComponent = ref(null)
    const id = ref(null)
    var summary = ref(null);
    var link1 = ref(null);
    var link2 = ref(null);
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
        header.style.height = "17em";
        title.style.fontSize = "15em";
        title.style.paddingTop = "0.32em";
        title.style.lineHeight = "3.125rem";
        title.style.paddingLeft = "0em";
        flavour.style.fontSize = "2em";
        flavour.style.opacity = "0.7";
      }
    }

    // function switchState() {
    //   console.log("state switched to summary screen");
    // }


// function insertSubs(data) {

//   const timestaps = Object.keys(data)
//   const summaries = Object.values(data)
//   const container = document.createElement("div")
//   container.id = "sub-summaries"
//   console.log(timestaps)
//   for (let i = 0; i < timestaps.length; i++) {
//     let div = document.createElement("div")
//     div.className = "sub-container"

//     let tag = document.createElement("p")
//     tag.className = "timestamp"

//     let sub = document.createElement("p")
//     sub.className = "sub"

//     tag.innerHTML = timestaps[i]
//     sub.innerHTML = summaries[i]

//     div.appendChild(tag)
//     div.appendChild(sub)

//     container.appendChild(div)
//   }
//   console.log(container)
//   subs.value = container
// }


const getData = async id => {
              Loading.show({
                message: "Generating summary",
                backgroundColor: "grey-4",
                customClass: "loading",
                spinnerColor: "accent",
                messageColor: "black"
              })
              try {
                console.log(id)
                const response = await api.get(URL_BASE + "/summarise/" + id)
                console.log(response)
                const data = response.data
                console.log(data)

                console.log(data.text.sub)
                summary.value = data.text.overall

                subs.value = data.text.sub
                console.log(subs.value)
                summary_ready.value = true;
                // insertSubs(data.text.sub)
              }
              catch (error) {
                console.log("REEEEEEE")
                Notify.create("The request has failed. i'm truly sorry.")
              }
                  Loading.hide()
            }



const getLinks = async id => {
      console.log(id)
      const response = await api.get(URL_BASE + "/links/" + id)
      console.log(response)
      const data = response.data
      link1.value = data.links.IR[0]
      link2.value = data.links.IR[1]
      links_ready.value = true;
    }

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


          function trigger() {
            const barRef = bar.value
            barRef.start()

            setTimeout(() => {
              const barRef = bar.value
              if (barRef) {
                barRef.stop()
              }
            }, Math.random() * 5000 + 1000)
          }




    return {
      id,
      bar,
      subs,
      trigger,
      get_id,
      embed_id,
      sum: summary_ready,
      text: summary,
      link1: link1,
      link2: link2,
      links: links_ready,

      onSubmit() {
        console.log("submit button pressed")
        const vid_id = get_id(id.value)
        if (vid_id) {
          trigger()
          getData(vid_id)
          getLinks(vid_id)
        }
        else {
          // error handling here
        }
      }



    };
  }
};

</script>
