import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {

  private readonly API = 'http://localhost:5000';
  static isLogged = false;

  constructor(private http: HttpClient) { }

  async create(user:any){
    const result = await this.http.post<any>(this.API + '/register/', user.value).toPromise()
    return result
  }

  async login(user: any){
    const result = await this.http.post<any>(this.API + '/login/',user.value).toPromise();
    if(result && result.data){
      window.localStorage.setItem('token', result.data)
      return true
    }
    return false
  }

  async isLogged(token:any){
    if(token){
      const result = await this.http.get<any>(this.API + '/register/', {
        headers: new HttpHeaders({
          'Content-Type':  'application/json',
          token: token
        })
      } ).toPromise()
      console.log(result)
      if(result.detail == "Unauthenticated!"){
        return {user: result, login: false}
      }
      else{
        return {user: result, login: true}
      }
    }
    return {login: false}
  }

  getToken(){
    const token = window.localStorage.getItem('token')
    return token
  }


  async getList(token:any, type:any){
    if(token){
      const result = await this.http.get<any>(this.API + '/manager/',{
        headers: new HttpHeaders({
          'Content-Type':  'application/json',
          token: token,
          type: type
        })
      } ).toPromise()
      return result
    }
  }

  async search(title:any, type:any){
    const result = await this.http.get<any>(this.API + '/search/',{
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
        title: title,
        type: type
      })
    } ).toPromise()
    return result
  }
  async searchId(id:any){
    const result = await this.http.get<any>(this.API + '/data/',{
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
        id: id,
        
      })
    } ).toPromise()
    return result
  }

  async addToList(att:any){
    const result = await this.http.post<any>(this.API + '/manager/',{
      token: this.getToken(),
      title: att.title,
      desc: att.desc,
      urlImg: att.urlImg,
      rating: att.rating,
      genre: att.genre,
      stream: att.stream,
      attractionType: att.attractionType
    }).toPromise()
    return result
  }
}
