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
          <p class="text-body1">Lorem ipsum dolor sit amet consectetur adipisicing elit. Eos unde dolores possimus maxime nihil officiis expedita repellat voluptatibus alias? Quod sed amet magni beatae error quidem ipsam nostrum vitae officiis. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odit fugiat voluptates perferendis aperiam rem consequuntur placeat, corrupti sit quod, itaque quam rerum? Aut illo deserunt quidem earum, magnam doloribus veritatis! Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aperiam reiciendis consequuntur expedita odio, error asperiores, vel, quibusdam beatae non recusandae eveniet. Aliquid quas vero aut, dignissimos labore aliquam ducimus tempore. Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque ipsum aliquid ullam eum atque rem cum voluptatibus magni aliquam eius optio totam laudantium, saepe doloremque corrupti necessitatibus dolor repellat blanditiis?</p>
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
