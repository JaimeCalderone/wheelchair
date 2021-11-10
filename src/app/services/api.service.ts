import { Injectable } from '@angular/core';
import { Observable, of, throwError } from 'rxjs';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { catchError, tap, map } from 'rxjs/operators';

const httpOptions = {
  headers: new HttpHeaders({'Content-Type': 'application/json'})
};
const apiUrl = "https://jsonplaceholder.typicode.com";

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  private handleError(error: any) {
    if (error.error instanceof ErrorEvent) {
      // A client-side or network error occurred. Handle it accordingly.
      console.error('An error occurred:', error.error.message);
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong,
      console.error(
        `Backend returned code ${error.status}, ` +
        `body was: ${error.error}`);
    }
    // return an observable with a user-facing error message
    return throwError('Something bad happened; please try again later.');
  }
  
  private extractData(res: Response) {
    let body = res;
    return body || { };
  }

  public getItems(): Observable<any> {
    return this.http.get(apiUrl + "/posts", httpOptions).pipe(
      map(this.extractData),
      catchError(this.handleError));
  }
  
  getItemById(id: string): Observable<any> {
    return this.http.get(apiUrl + "/" + id, httpOptions).pipe(
      map(this.extractData),
      catchError(this.handleError));
  }
  
  postItem(data): Observable<any> {
    return this.http.post(apiUrl, data, httpOptions)
      .pipe(
        catchError(this.handleError)
      );
  }
  
  updateItem(id: string, data): Observable<any> {
    return this.http.put(apiUrl + "/" + id, data, httpOptions)
      .pipe(
        catchError(this.handleError)
      );
  }
  
  deleteItem(id: string): Observable<{}> {
    return this.http.delete(apiUrl + "/" + id, httpOptions)
      .pipe(
        catchError(this.handleError)
      );
  }
}
