

import pugPlugin from "@11ty/eleventy-plugin-pug";
import sassPlugin from "eleventy-sass";
import { RenderPlugin } from "@11ty/eleventy";

export default async function(eleventyConfig) {
	// Configure Eleventy
    eleventyConfig.addPlugin(pugPlugin);
    eleventyConfig.addPlugin(sassPlugin);
    eleventyConfig.addPlugin(RenderPlugin);

    eleventyConfig.addPassthroughCopy("src/assets/css/img/*");

    // eleventyConfig.addCollection("events", function (collectionAPI) {
    //     return collectionAPI.getFilteredByGlob("./_events/*.md");
    //   });
    eleventyConfig.addCollection(
        "events",
        collection => collection.getFilteredByGlob(`./_events/*`)
    )

    // eleventyConfig.addCollection(
    //     "faq",
    //     collection => collection.getFilteredByGlob(`./_faq/*`)
    // )
};

export const config = {
    dir: {
      input: "src",
      layouts: "_includes/layouts"
    }
  };