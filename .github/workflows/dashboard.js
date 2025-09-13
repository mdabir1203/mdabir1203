const fs = require("fs");
const axios = require("axios");
const figlet = require("figlet");

(async () => {
  // ====== Fetch random hacker/dev wisdom ======
  let quote = "Hack the planet!"; // fallback
  try {
    // Example: Programming Quotes API
    const res = await axios.get("https://programming-quotes-api.herokuapp.com/quotes/random");
    quote = `${res.data.en} — *${res.data.author}*`;
  } catch (e) {
    // fallback to Adviceslip
    try {
      const res = await axios.get("https://api.adviceslip.com/advice");
      quote = JSON.parse(res.data).slip.advice;
    } catch (err) {
      // silent fail, keep fallback tip
    }
  }

  // Example: Get your GitHub stats
  const ghUser = "mdabir1203";
  const ghData = (await axios.get(`https://api.github.com/users/${ghUser}`)).data;

  // ASCII Banner
  const banner = figlet.textSync("HACK THE CODE", { font: "Cyberlarge" });

  // Regenerate README.md
  const readme = `
# 🕶️ Hacker's Dashboard

\`\`\`
${banner}
\`\`\`

**💻 GitHub Hacker Stats**
- Followers: ${ghData.followers}
- Public Repos: ${ghData.public_repos}

**⚡ Hacker Tip of the Day**  
> ${tip}

![Contribution Graph](https://github-readme-activity-graph.vercel.app/graph?username=${ghUser}&theme=tokyo-night)

---
⚔️ *Automated update every 6h by a secret hacker agent...*
`;

  fs.writeFileSync("README.md", readme);
})();
