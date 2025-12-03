// nuxt.config.ts
export default defineNuxtConfig({
  ssr: false,

  app: {
    head: {
      title: "SEO Audit Tool",
      meta: [{ name: "viewport", content: "width=device-width, initial-scale=1" }],
      link: [
        { rel: "stylesheet", href: "/styles.css" } // custom CSS file
      ]
    }
  }
});
