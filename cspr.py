// Loon 脚本示例

// 初始化一个集合来保存 authorization 值
let authSet = new Set();

// 处理请求
function handleRequest(request) {
    if (request.method === "GET" && request.url.startsWith("https://api.cspr.community/api/users/me")) {
        let authHeader = request.headers["authorization"];
        if (authHeader) {
            console.log(`Authorization header: ${authHeader}`); // 调试信息
        }
    }
}

// 处理响应
function handleResponse(response) {
    if (response.statusCode === 200 && response.request.method === "GET" && response.request.url.startsWith("https://api.cspr.community/api/users/me")) {
        let authHeader = response.request.headers["authorization"];
        if (authHeader && !authSet.has(authHeader)) {
            authSet.add(authHeader);
            console.log(`Captured authorization: ${authHeader}`); // 调试信息
            saveAuthValues();
        }
    }
}

// 保存 authorization 值到本地存储
function saveAuthValues() {
    let authArray = Array.from(authSet);
    $persistentStore.write(JSON.stringify(authArray), "auth_values");
    console.log("Saved authorization to local storage"); // 调试信息
}

// 注册请求和响应处理器
$httpClient.on("request", handleRequest);
$httpClient.on("response", handleResponse);
