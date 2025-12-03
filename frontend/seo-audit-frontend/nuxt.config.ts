export default defineNuxtConfig({
  ssr: false,                      // 🔥 build static /dist/ folder
  target: "static",                // 🔥 ensure SSG output format
  modules: ["@nuxtjs/tailwindcss"],
  css: ["~/assets/css/tailwind.css"],
// devtools: { enabled: true },
  build: {
    transpile: [],
  }
})
