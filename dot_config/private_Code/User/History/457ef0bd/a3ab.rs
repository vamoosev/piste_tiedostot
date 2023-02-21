use actix_web::{get, web, App, HttpServer, Responder};
use serde_json;
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
    let user = User{Name: name,Passwordhash: String::from("2"), Name=String::from(name), Passwordhash=String::from("2") };
    format!("{}", serde_json::to_string(&user).unwrap())
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().service(index).service(hello))
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
}