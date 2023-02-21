use actix_web::{get, web, App, HttpServer, Responder};
use serde_json;
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
struct User{
    Name: String,
    Passwordhash: String,
}



#[get("/")]
async fn index() -> impl Responder {
    "Hello, World!"
}

#[get("/{name}")]
async fn hello(name: web::Path<String>) -> impl Responder {
    let user = User{
        Name: name.to_string(),
        Passwordhash: "123".to_string(),
    };

    let json = serde_json::to_string(&user).unwrap() ;
    format!("{}", json)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().service(index).service(hello))
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
}