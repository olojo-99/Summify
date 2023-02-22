<template>
  <q-page id="main-container" class="flex">

    <div v-if="sum == false" id="search-container" class="flex flex-center flex-item column">

      <div id="description" class="flex-item">
        <p>Summify is a college project that summarises Youtube transcripts.</p>
        <p>Enter a Youtube video link and click submit to generate a summarised transcript.</p>
        <p>Videos that do not have captions or have captions turned off by the author will not work.</p>
      </div>

      <div id="search-bar" class="flex-item">
        <q-form ref="formComponent" @submit.prevent>
          <div id="bar-button">
            <q-input v-model="id" error-message="Please enter a valid Youtube video" name="id" filled type="url"
              outlined label="Insert Youtube Video URL" for="link-input" />
              <q-ajax-bar
            id="ajax"
            ref="bar"
            position="bottom"
            color="accent"
            size="20px"
          />

            <q-btn @click="onSubmit" id="submit-button" label="Submit" type="submit" color="primary" />
          </div>
        </q-form>
      </div>
    </div>

    <!-- Request returned -->

    <div v-else id="content" class="flex row">

      <!-- left column -->
      <div id="left" class="flex-item">
        <div id="video-embed">
          <iframe v-bind:src="embed_id(get_id(id))" title="YouTube video player" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen></iframe>
        </div>


        <div v-if="links_ready == 'A'" id="right" class="flex-items">
          <q-spinner color="accent" size="10em" />
          <h5 class="text-h5">Retrieving information from summary: Generating links</h5>


        </div>

        <div v-else-if="links_ready == 'B'" id="links">
          <div id="link-container" class="flex column">


            <a v-for="link in links" v-bind:key="link" :href="link.url" target="_blank" class="flex link">
              <q-card class="q-pt-none" flat square>
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


          </div>
        </div>

        <div v-else-if="links_ready == 'C'" id="links-error">
          <p>Related links unavailable, something went wrong on our end.</p>
        </div>
      </div>






      <!-- middle column -->
      <div id="middle" class="flex-item">

        <div id="transcript-text">
          <h2>General Summary:</h2>
          <p id="summary-body" class="text-body1">{{ text }}
          </p>

          <h2>5 Minute Segments:</h2>


          <div id="sub-summaries" class="text-body1">
            <div v-for="(value, key) in subs" v-bind:key="key" class="sub-summary">
              <span class="timestamp">{{ key }}: </span>{{ value }}
            </div>
          </div>



        </div>

      </div>


    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import axios, { api } from 'boot/axios'
import { Loading, Notify, QSpinnerGears, LoadingBar } from 'quasar'

const refComponent = ref(null)
const id = ref(null)
var summary = ref(null);
var links = ref(null);
var subs = ref(null)
var URL_BASE = "http://127.0.0.1:5000"
const summary_ready = ref(false);
const links_ready = ref('A')

// sending youtube video id to backend
const getData = async id => {

  try {
    // displaying the loading box and spinner
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
    // vue dynamic rendering to change page layout and display summaries
    summary_ready.value = true;
    Loading.hide()


    // second call to backend to get information retrieval links
    // call made after the first one completes as backend needs to fully process summaries before it does IR
    console.log('getting links')
    try {
      const response2 = await api.get(URL_BASE + "/links/" + id)
      console.log(response2)
      const data2 = response2.data
      console.log(data2)
      links.value = data2
      links_ready.value = 'B';
    }
    catch (err) {
      if (err.response) {
        if (err.response.status == 580) {
          console.log(err.response.status)
          links_ready.value = 'C'
          Notify.create("Related links unavailable.")
        }
      }
    }
    
  }
  catch (err) {
    // error handling different cases
    if (err.response) {
      if (err.response.status == 560) {
        Notify.create("Transcript unavailable for this video.")
      }
      else if (err.response.status == 550) {
        Notify.create("Video exceeds maximum length.")
      }
      else if (err.response.status == 570) {
        Notify.create("GPT-3 Unavailable.")
      }
      // else if (err.response.status == 580) {
      //   Notify.create("Custom Google Search Engine Unavailable.")
      // }
      else {
        Notify.create("We're sorry, something went wrong on our end.")
      }
    }
    console.log(err.response)
    console.log("Error processing the request")

    Loading.hide()
  }
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
