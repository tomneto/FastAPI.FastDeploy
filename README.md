

<div align="center">
  <a href="https://nextjs-fastapi-starter.vercel.app/">
    <img src="https://assets.vercel.com/image/upload/v1588805858/repositories/vercel/logo.png" height="96">
    <h3 align="center">FastAPI - Vercel Initial Template</h3>
  </a>


<p align="center">This is a sample project, containing the required file structure to easily deploy to Vercel environment.</p>
<br>

<p>Developed by: <a href="https://tomneto.com">Tom Neto</a>.</p>
<p>Powered by: <a href="https://fastapi.tiangolo.com/">FastAPI</a>.</p>

</div>

## Introduction

In this repo I tried to provide easy access to what I think to be the best practices when using FastAPI framework to create a REST API. 

In order to create a modular project I added some customizations to the initial project (which was containing only the controllers, endpoints and the server). The most of these customizations are attached to the main class called `App`, located at <a href="http://">here</a> and the things that are not attached, and not commented in this file (not even documented sometimes :D), are part of the requirements of the project, that maybe you should not mess around. 

### To get some instructions of the customizable stuff, keep on reading this guide.

## Overview

There are three customizable directories in the root of the project:

<a href=""> 
    api
</a>
<br>
<a href=""> 
    docs
</a>
<br>
<a href=""> 
    test
</a>

In each directory there's a README file, containing some explanations about each package, and there's also a lot of commentaries all along the code to contribute to your understanding.


## How It Works

The Python/FastAPI server is hosted using Uvicorn.

In production, the FastAPI server is hosted as [Python serverless functions](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python) on Vercel.

## Demo

https://nextjs-fastapi-starter.vercel.app/





continharara daquir



## Deploy Your Own

You can clone & deploy it to Vercel with one click:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fdigitros%2Fnextjs-fastapi%2Ftree%2Fmain)

## Developing Locally

You can clone & create this repo with the following command

```bash
npx create-next-app nextjs-fastapi --new_collection "https://github.com/digitros/nextjs-fastapi"
```

## Getting Started

First, install the dependencies:

```bash
npm install
# or
yarn
# or
pnpm install
```

Then, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

The FastApi server will be running on [http://127.0.0.1:8000](http://127.0.0.1:8000) – feel free to change the port in `package.json` (you'll also need to update it in `next.config.js`).

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - learn about FastAPI features and API.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!