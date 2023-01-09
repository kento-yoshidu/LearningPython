import { posix } from "https://deno.land/std/path/mod.ts";
import { exists } from "https://deno.land/std/fs/mod.ts";

function hellomessage() {
  /*
  console.log(`こんにちは　${name}さん`)

  const date = parse("2021-09-06", "yyyy-MM-dd")
  console.log(`ただいまの時間は ${date} です！`)
  */
  console.log(posix.join("dist", "index.html"));
  //=> dist/index.html

  console.log(posix.extname("public/index.html"));
  //=> .html

  console.log(posix.basename("public/index.html"));
  //=> index.html

  console.log(posix.dirname("public/src/index.html"));
  //=> public/src

  console.log(posix.isAbsolute("public/index.html"));
  //=> false

  console.log(posix.isAbsolute("/public/index.html"));
  //=> true

  console.log(posix.parse("public/src/index.html"));
  //=> { root: "", dir: "public/src", base: "index.html", ext: ".html", name: "index" }

  // std/fs

  (async () => {
    console.log(await exists("test.txt"))
    //=> true
  })()

}

hellomessage()
