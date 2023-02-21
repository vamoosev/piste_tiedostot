use actix_web::{get, web, App, HttpServer, Responder};
use serce_json;
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
        Name = name,
        Passwordhash = "2",
    };

}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().service(index).service(hello))
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
}