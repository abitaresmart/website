---
layout: home
---

<div class="container max-w-screen-md py-12 md:py-12 mx-auto px-4 sm:px-6 lg:px-8">
    <h1 class="text-4xl font-black">Blog</h1>
  <ul class="mt-12">
    {%- for post in site.posts -%}
    <li class="mt-16 list-reset">
      <time class="uppercase text-xs text-gray-500 font-bold">{{ post.date | date: "%b %-d, %Y" }}</time>
      <h2 class="mt-1 text-2xl tracking-tight font-extrabold text-gray-900 sm:leading-none md:text-3xl">
        <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
      </h2>
      <div class="content flex py-2">
        <img class="w-48 md:w-64 rounded-lg self-start" src="/assets/img/blog/thumb/{{post.image}}" alt="">
        <div class="post-content px-2">
          {{ post.excerpt }}
        </div>
      </div>
      <div class="mt-10">
        <a class="bg-main-400 hover:bg-main-700 text-white font-bold py-2 px-4 rounded-full" href="{{ post.url | relative_url }}">Leggi di più
        </a>
      </div>
    </li>
    <hr class="w-full bg-gray-100 my-12" style="height: 1px;">
     {%- endfor -%}
  </ul>
</div>