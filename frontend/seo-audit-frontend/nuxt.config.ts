export default defineNuxtConfig({
  nitro: { preset: "netlify" },

  app: {
    head: {
      script: [
        {
          src: "https://cdn.tailwindcss.com",
          defer: false
        }
      ]
    }
  }
})
