const api = axios.create({
  baseURL: "",
  // timeout: 5000,
  headers: {
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
  },
});
