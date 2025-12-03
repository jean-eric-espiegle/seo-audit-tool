// nuxt.config.ts
export default defineNuxtConfig({
  ssr: false, // for static SPA output
  devtools: { enabled: false },

  // Inject CDN tailwind without breaking Vite
  app: {
    head: {
      link: [
        {
          rel: "stylesheet",
          href: "https://cdn.jsdelivr.net/npm/tailwindcss@3.4.10/dist/tailwind.min.css"
        }
      ]
    }
  }
});
