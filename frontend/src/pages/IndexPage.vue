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
        <p>Enter a longform Youtube link (eg. https://www.youtube.com/watch?v=dQw4w9WgXcQ)</p>
        <p>Videos that do not have captions or have captions turned off by the author will not work.</p>
      </div>

      <div
        id="search-bar"
        class="flex-item">
        <q-form
          id="url_submission"
          @submit.prevent>
          <q-input
            v-model="url"
            name="video_url"
            filled
            type="url"
            outlined
            label="Insert Video URL"
          />
          <q-btn
            id="submit-button"
            label="Submit"
            type="submit"
            color="primary" />
        </q-form>
      </div>
    </div>

    <div
      v-else
      id="content"
      class="flex row">
      <div
        id="left"
        class="flex-item">
      </div>
      <div
        id="middle"
        class="flex-item">
        <div id="video-embed">
          <iframe
            width="560"
            height="315"
            src="https://www.youtube.com/embed/U_gANjtv28g"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen></iframe>
        </div>
        <div id="transcript-text">
          <h1 class="text-h1">Summary</h1>
          <p
            id="summary-body"
            class="text-body1">{{ text }}</p>
        </div>
      </div>

      <div
        id="right"
        class="flex-item">
        <div id="links">
<a
href="http://www.google.com"
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
              example.com
            </q-card-section>
          </q-card>

</a>

<a
href="http://www.google.com"
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
              example.com
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
import { api } from 'boot/axios'
// import { useQuasar } from 'quasar'
// import { response } from "express";
// import { data } from "browserslist";




// const urlSubmission = document.getElementById('url_submission')
// function submitForm (event) {
//   event.preventDefault()
//   let http = new XMLHttpRequest()
//   http.open('GET', 'BACKEND_URL', true)
//   http.setRequestHeader('Constant-type', 'application/x-www-form-urlencoded')
//   let params = 'search=' +
// }
// if (urlSubmission) urlSubmission.addEventListener('submit', submitForm)

// function switchToSummarised() {
//   Document.
// }

function init() {
  var button = document.getElementById('submit-button');
  button.addEventListener("click", switchState);

}

var summary = ref("");

window.onload = init;


const summary_ready = ref(false);

function switchState() {
  console.log("state switched to summary screen");
  summary_ready.value = true;
  api.get('http://127.0.0.1:5000')
      .then((response) => {
        console.log(response)
        summary.value = response.data
      })
      .then(() => {
        console.log(summary)
        var sum_text = document.getElementById("summary-body")
      }
      )
}


export default {
  data() {
    return {
      sum: summary_ready,
      text: summary
    };
  }

}

;


// export default defineComponent({
//   name: "IndexPage",
// });
</script>
