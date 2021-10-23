interface IQuery {
  page: number;
  perPage: number;
}
export const paginationSerializer = (
  total: number,
  query: IQuery
): {
  perPage: number;
  total: number;
  page: number;
  prevPage: number | null;
  nextPage: number | null;
  totalPages: number;
} => {
  const { page, perPage } = query;
  // si el total es mayor o igual que los items por pagina entonces los items seran el perPage, caso contrario sera el total
  const itemsPerPage = total >= perPage ? perPage : total;
  // dividir el total entre los items por pagina y si esta es una division inexacta entonces agarrraremos el proximo numero entero
  const totalPages = Math.ceil(total / itemsPerPage);

  // si la pagina actual es mayor que 1 Y la pagina es menor o igual que el total de paginas (fue una busqueda correcta) entonces si habra pagina previa, caso contrario no
  const prevPage = page > 1 && page <= totalPages ? page - 1 : null;

  // indicara si hay mas de una pagina y ademas si la pagina actual es menor que la cantidad total de paginas sino sera nulo
  const nextPage = totalPages > 1 && page < totalPages ? page + 1 : null;

  return {
    perPage: itemsPerPage,
    total,
    page,
    prevPage,
    nextPage,
    totalPages,
  };
};

export const paginationHelper = ({
  page,
  perPage,
}: IQuery): { skip: number; limit: number } | void => {
  if (page && perPage) {
    return {
      skip: (page - 1) * perPage,
      limit: perPage,
    };
  }
};
