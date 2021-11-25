import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {

  private readonly API = 'http://localhost:8000/api';
  static isLogged = false;

  constructor(private http: HttpClient) { }

  create(user:any){
    return this.http.post(this.API + '/register/', user)
  }

  login(user:any){
    return this.http.post(this.API + '/login/', user)
  }
}
