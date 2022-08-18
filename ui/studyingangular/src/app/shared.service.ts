import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {

  readonly APIUrl = "http://127.0.0.1:8000/";
  readonly PhotoUrl = "http://127.0.0.1:8000/media/";

  constructor(private http:HttpClient) { }

  //departament methods
  getDepList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/departament/');
  }

  addDepartament(val:any){
    return this.http.post(this.APIUrl + '/departament/', val);
  }

  updateDepartament(val:any){
    return this.http.put(this.APIUrl + '/departament/', val);
  }

  deleteDepartament(val:any){
    return this.http.delete(this.APIUrl + '/departament/' +val);
  }

//employee methods

  getEmpList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/departament/');
  }

  addEmployee(val:any){
    return this.http.post(this.APIUrl + '/employee/', val);
  }

  updateEmployee(val:any){
    return this.http.put(this.APIUrl + '/employee/', val);
  }

  deleteEmployee(val:any){
    return this.http.delete(this.APIUrl + '/employee/' +val);
  }

  //save profile picture

  UploadPhoto(val:any){

    return this.http.post(this.APIUrl + '/SaveFile', val);

  }

  //get departament names
  getAllDepartamentNames():Observable<any[]>{
    
    return this.http.get<any[]>(this.APIUrl + '/departament/');

  }
}
