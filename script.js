console.log("Hello via Bun!");
Bun.serve({
    port: 3000,
    fetch(req) {
      return new Response("Hello from Webhook!");
    },
  });