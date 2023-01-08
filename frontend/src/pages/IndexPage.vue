<template>
  <q-page class="flex flex-center">
    <div v-if="sum == false">
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
    <div v-else>
      <div id="video-embed"><iframe
          width="560"
          height="315"
          src="https://www.youtube.com/embed/U_gANjtv28g"
          title="YouTube video player"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          allowfullscreen></iframe>
      </div>
      <div id="transcript-text"></div>
      <div id="links"></div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
// import { api } from 'boot/axios'
// import { useQuasar } from 'quasar'
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

window.onload = init;


const summary_ready = ref(false);

function switchState() {
  console.log("lol");
  summary_ready.value = true;
}


export default {
  data() {
    return {
      sum: summary_ready
    };
  }
};


// export default defineComponent({
//   name: "IndexPage",
// });
</script>
