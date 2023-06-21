<header align="center" class="header">

<a align="center" class="fastApiLogo" href="https://fast-api-fast-deploy.vercel.app/">
    <img align="center" src="https://cdn.worldvectorlogo.com/logos/fastapi-1.svg" height="96">
    <div align="center"> 
        <h3 align="center" class="title">FastAPI + FastDeploy</h3>
    </div>
  </a>

</header>
<div>
<h2>Introduction</h2>

<p class="intro">This is a Python sample project, containing the required file structure to easily deploy to Vercel, Docker or Replit environments. It is powered by FastAPI and MongoDB. The most of my projects were using this kind of environment and architecture, so I decided to put it in a public repository so everyone can enjoy and contribute.
</p>

<div class="adviceEnclosure"> 
<h3 class="advice">Here are some customization tips</h3>
</div>
<div class="tipNameEnclosure"> 
<p>   - Understanding the file structure </p>
</div>

<p>
    This project was developed to delivery easier access for some of the customizations that we always need to do while performing deployment to the Docker, Replit or Vercel environments. But in the counter hand it came with some routing, controllers, middleware which are commonly used in Node.js or TypeScript implementations. This architecture has been developed to deliver a great readability of the code. But it is quite confusing if you're not into it.
</p>
<div class="alertEnclosure">
<p class="alert">So I highly recommend to start at least one project by yourself, without using this "shortcut". </p>
</div>


<div class="tipNameEnclosure"> 
<p>    - Find out for the "new" tag </p>
</div>

While we're coding API's it's a common practice to create the basic methods we are going to use and copy the same basic code just by changing models, descriptions, controllers, and so on. In this project you're going to find this basic methods, so you can simply add your special touch and you're ready to go. To easy manipulate this code, I add the "new" prefix to this replacable part of the code. Like this:

<a href="https://ibb.co/jH8vKdx"><img src="https://i.ibb.co/t3HMfSN/Screenshot-2023-06-18-at-19-23-49.png" alt="Screenshot-2023-06-18-at-19-23-49" border="0"></a>

These code was obtained in one of the default endpoint files included in the project, by copying and manipulating this code in order to create a new get route we can simply get this code and replace the "new_" with "whatever_you_want". And you will have a basic get endpoint with the most common error handlers already loaded. But of course this is just the tip of the iceberg.

</div>
<br>

<p>Developed by: <a href="https://tomneto.com">Tom Neto</a>.</p>

<div>
<h3>Powered by:</h3>
<lu>
    <img class="fastapiMini" src="https://cdn.worldvectorlogo.com/logos/fastapi-1.svg" height="25"><a href="https://fastapi.tiangolo.com/">FastAPI</a>.
</lu>
<lu>
    <img class="vercelMini" src="https://assets.vercel.com/image/upload/v1588805858/repositories/vercel/logo.png" height="26"><a href="http://vercel.com/">Vercel</a>.
</lu>

<lu>
    <img class="dockerMini" src="https://i.ibb.co/zrxvKM6/docker.png" height="20"><a href="https://www.docker.com/">Docker</a>.
</lu>

</div>
