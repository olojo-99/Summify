<template>
  <q-page class="flex flex-center">
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
        to="/summarised"
        id="submit-button"
        label="Submit"
        type="submit"
        color="primary" />
    </q-form>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
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



export default defineComponent({
  name: "IndexPage",
});
</script>
