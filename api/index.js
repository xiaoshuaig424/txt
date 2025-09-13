export default async function handler(req, res) {
  const url = "https://api.xygeng.cn/one";
  const response = await fetch(url);
  const data = await response.json();

  const text = `${data.data.content} —— ${data.data.origin}`;
  res.setHeader("Content-Type", "text/plain; charset=utf-8");
  res.send(text);
}
